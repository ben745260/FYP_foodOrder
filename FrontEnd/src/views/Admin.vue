<template>
  <div class="admin-panel">
    <div class="container-fluid h-100">
      <div class="row h-100">
        <div class="col-md-2 p-0">
          <div class="side-bar d-flex flex-column flex-shrink-0 p-3 text-white bg-dark h-100">
            <router-link to="/admin/dashboard"
              class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none">
              <h2 class="fw-bold">Food Ordering System</h2>
            </router-link>
            <hr>
            <ul class="nav nav-pills flex-column mb-auto">
              <li>
                <router-link to="/admin/dashboard" class="nav-link" active-class="active">
                  <i class="fa fa-home"></i> Dashboard
                </router-link>
              </li>
              <li>
                <router-link to="/admin/orders" class="nav-link" active-class="active">
                  <i class="fa fa-shopping-cart"></i> Orders
                </router-link>
              </li>
              <li>
                <router-link to="/admin/tables" class="nav-link" active-class="active">
                  <i class="fa fa-table"></i> Tables
                </router-link>
              </li>
              <li>
                <router-link to="/admin/menus" class="nav-link" active-class="active">
                  <i class="fa fa-bars"></i> Menus
                </router-link>
              </li>
            </ul>
            <hr>
            <div class="dropdown">
              <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle"
                id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
                <span>{{ username }}</span>
              </a>
              <ul class="dropdown-menu dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser1">
                <li>
                  <router-link to="/admin/settings" class="dropdown-item">
                    Settings 
                  </router-link>
                </li>
                <li>
                  <hr class="dropdown-divider">
                </li>
                <li><button class="dropdown-item" @click="logout">Sign out</button></li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col-md-10 p-0">
          <div class="bg-body-tertiary h-100 px-5 py-3">
            <router-view></router-view>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: this.$store.state.username
    };
  },
  methods: {
    logout() {
      this.$store.commit('removeToken');
      location.reload(true);
    }
  }
};
</script>

<style scoped>
.admin-panel {
  height: 100vh;
}

.side-bar {
  font-weight: 600;
  color: white;
}

.nav-link {
  color: white;
}

.nav-link i {
  margin-right: 10px;
}

.nav-link:hover {
  background-color: #384454
}

.nav-link.active {
  background-color: #384454
}</style>